import React, { useEffect, useRef, useState } from 'react';
import WaveSurfer from 'wavesurfer.js';
import { supabase } from './supabaseClient';

export default function App() {
const containerRef = useRef(null);
const wavesurferRef = useRef(null);
const [isPlaying, setIsPlaying] = useState(false);
const [currentTime, setCurrentTime] = useState(0);
const [duration, setDuration] = useState(0);

// 초기 샘플 댓글 및 로컬 스토리지 연동
const [comments, setComments] = useState(() => {
const saved = localStorage.getItem('studio_comments');
if (saved) {
try { return JSON.parse(saved); } catch (e) { /* ignore */ }
}
return [
{ id: 1, track_id: 1, author: '인디 프로듀서', timestamp_seconds: 1.0, text: '도입부 사운드 느낌 아주 좋네요!' },
{ id: 2, track_id: 1, author: '믹싱 엔지니어', timestamp_seconds: 2.5, text: '여기 볼륨 살짝만 다듬으면 완벽할 것 같아요.' }
];
});

const [newCommentText, setNewCommentText] = useState('');
const trackId = 1;

// 댓글 변경 시 로컬 스토리지에 자동 동기화
useEffect(() => {
localStorage.setItem('studio_comments', JSON.stringify(comments));
}, [comments]);

// 웨이브폼 초기화 (MDN 공식 테스트 오디오 CDN 적용 - 403 및 CORS 문제 없음)
useEffect(() => {
if (!containerRef.current) return;

const ws = WaveSurfer.create({
container: containerRef.current,
url: 'https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3', // 100% 안전한 개발용 테스트 오디오
waveColor: '#d1d5db',
progressColor: '#6366f1',
cursorColor: '#4f46e5',
height: 80,
});

wavesurferRef.current = ws;

ws.on('ready', () => setDuration(ws.getDuration()));
ws.on('audioprocess', () => setCurrentTime(ws.getCurrentTime()));
ws.on('play', () => setIsPlaying(true));
ws.on('pause', () => setIsPlaying(false));

ws.on('error', (err) => {
console.warn('WaveSurfer 오디오 로드 경고:', err);
});

return () => ws.destroy();
}, []);

// 코멘트 등록하기
const handleAddComment = async (e) => {
e.preventDefault();
if (!newCommentText.trim() || !wavesurferRef.current) return;

const currentSeconds = wavesurferRef.current.getCurrentTime();
const newCommentObj = {
id: Date.now(),
track_id: trackId,
author: '나 (아티스트)',
timestamp_seconds: Number(currentSeconds.toFixed(2)),
text: newCommentText
};

// Supabase 연동 시도 (실패 시 로컬 스토리지에 안전하게 반영)
try {
const { data, error } = await supabase
.from('track_comments')
.insert([{
track_id: trackId,
author: '나 (아티스트)',
timestamp_seconds: Number(currentSeconds.toFixed(2)),
text: newCommentText
}])
.select();

if (!error && data && data.length > 0) {
setComments(prev => [...prev, data[0]].sort((a, b) => a.timestamp_seconds - b.timestamp_seconds));
} else {
setComments(prev => [...prev, newCommentObj].sort((a, b) => a.timestamp_seconds - b.timestamp_seconds));
}
} catch (err) {
setComments(prev => [...prev, newCommentObj].sort((a, b) => a.timestamp_seconds - b.timestamp_seconds));
}

setNewCommentText('');
};

// 시간 포맷 함수
const formatTime = (secs) => {
const m = Math.floor(secs / 60);
const s = Math.floor(secs % 60);
return `${m}:${s < 10 ? '0' : ''}${s}`;
};

return (
<div style={{ maxWidth: '600px', margin: '40px auto', padding: '24px', background: '#fff', borderRadius: '16px', boxShadow: '0 4px 12px rgba(0,0,0,0.05)', fontFamily: 'sans-serif' }}>
<h2 style={{ fontSize: '20px', fontWeight: 'bold', marginBottom: '4px' }}>클라우드 협업 스튜디오</h2>
<p style={{ fontSize: '14px', color: '#666', marginBottom: '20px' }}>인디 뮤지션 포트폴리오 & 타임스탬프 피드백</p>

{/* 웨이브폼 영역 */}
<div ref={containerRef} style={{ width: '100%', marginBottom: '20px', background: '#f8fafc', borderRadius: '8px' }} />

<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
<button
onClick={() => wavesurferRef.current?.playPause()}
style={{ padding: '8px 16px', background: '#6366f1', color: '#fff', border: 'none', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}
>
{isPlaying ? '일시정지' : '재생'}
</button>
<span style={{ fontFamily: 'monospace', fontSize: '14px' }}>
<b>{formatTime(currentTime)}</b> / {formatTime(duration)}
</span>
</div>

<form onSubmit={handleAddComment} style={{ display: 'flex', gap: '8px', marginBottom: '24px' }}>
<input
type="text"
value={newCommentText}
onChange={(e) => setNewCommentText(e.target.value)}
placeholder={`현재 위치(${formatTime(currentTime)})에 의견 남기기...`}
style={{ flex: 1, padding: '10px 14px', border: '1px solid #ddd', borderRadius: '8px', outline: 'none' }}
/>
<button
type="submit"
style={{ padding: '10px 16px', background: '#111', color: '#fff', border: 'none', borderRadius: '8px', cursor: 'pointer' }}
>
등록
</button>
</form>

<div>
<h3 style={{ fontSize: '15px', fontWeight: 'bold', marginBottom: '12px' }}>실시간 피드백 ({comments.length})</h3>
<div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '250px', overflowY: 'auto' }}>
{comments.map((c) => (
<div
key={c.id || Math.random()}
onClick={() => wavesurferRef.current?.setTime(Number(c.timestamp_seconds))}
style={{ padding: '12px', background: '#f9fafb', borderRadius: '8px', cursor: 'pointer', border: '1px solid #eee' }}
>
<span style={{ display: 'inline-block', padding: '2px 6px', background: '#e0e7ff', color: '#4338ca', fontSize: '12px', fontWeight: 'bold', borderRadius: '4px', marginRight: '8px' }}>
{formatTime(Number(c.timestamp_seconds))}
</span>
<span style={{ fontSize: '12px', fontWeight: 'bold', color: '#333' }}>{c.author}</span>
<p style={{ fontSize: '14px', color: '#555', margin: '4px 0 0 0' }}>{c.text}</p>
</div>
))}
</div>
</div>
</div>
);
}
