import React, { useEffect, useRef, useState } from 'react';
import WaveSurfer from 'wavesurfer.js';

export default function App() {
const [isPlaying, setIsPlaying] = useState(false);
const [isSequentialPlaying, setIsSequentialPlaying] = useState(false);
const [currentTime, setCurrentTime] = useState(0);
const [duration, setDuration] = useState(0);

const [trackList, setTrackList] = useState([
{
id: 1,
title: '🎤 보컬 스템 (Vocal Track)',
url: 'https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3',
muted: false,
comments: [
{ id: 101, author: '인디 프로듀서', timestamp_seconds: 1.0, text: '보컬 도입부 톤이 아주 매력적이네요.' }
],
newCommentText: ''
},
{
id: 2,
title: '🎸 악기 및 신스 스템 (Instrumental)',
url: 'https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3',
muted: false,
comments: [
{ id: 201, author: '믹싱 엔지니어', timestamp_seconds: 2.5, text: '신스 리버브 양을 살짝 줄이면 좋겠어요.' }
],
newCommentText: ''
},
{
id: 3,
title: '🥁 드럼 및 베이스 스템 (Drums & Bass)',
url: 'https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3',
muted: false,
comments: [],
newCommentText: ''
}
]);

const wavesurferRefs = useRef({});
const containerRefs = useRef({});

// 순차적 재생 상태 관리를 위한 Ref (비동기 이벤트 내부 최신 값 참조용)
const isSequentialRef = useRef(false);
const sequentialIndexRef = useRef(0);
const trackListRef = useRef(trackList);
trackListRef.current = trackList;

// WaveSurfer 초기화 및 순차 재생 이벤트 리스너 설정
useEffect(() => {
let isMounted = true;

trackList.forEach((track, index) => {
const container = containerRefs.current[track.id];
if (!container) return;

if (wavesurferRefs.current[track.id]) {
wavesurferRefs.current[track.id].destroy();
}

const ws = WaveSurfer.create({
container: container,
url: track.url,
waveColor: '#cbd5e1',
progressColor: '#6366f1',
cursorColor: '#4f46e5',
height: 50,
});

wavesurferRefs.current[track.id] = ws;

ws.on('ready', () => {
if (!isMounted) return;
const dur = ws.getDuration();
if (dur > duration) setDuration(dur);
});

ws.on('audioprocess', () => {
if (!isMounted) return;
if (track.id === trackListRef.current[0].id && !isSequentialRef.current) {
setCurrentTime(ws.getCurrentTime());
}
});

// 개별 트랙 재생 완료 시 처리
ws.on('finish', () => {
if (!isMounted) return;

// 순차적 재생 모드일 때 다음 트랙으로 자동 전환
if (isSequentialRef.current) {
ws.pause();
const currentIndex = sequentialIndexRef.current;
const nextIndex = currentIndex + 1;
const tracks = trackListRef.current;

if (nextIndex < tracks.length) {
sequentialIndexRef.current = nextIndex;
// 이전 트랙 음소거 및 다음 트랙 솔로 재생
const prevTrackId = tracks[currentIndex].id;
const nextTrackId = tracks[nextIndex].id;

wavesurferRefs.current[prevTrackId]?.setMuted(true);
const nextWs = wavesurferRefs.current[nextTrackId];
if (nextWs) {
nextWs.setMuted(false);
nextWs.setTime(0);
nextWs.play();
}
} else {
// 모든 트랙 순차 재생 완료
isSequentialRef.current = false;
setIsSequentialPlaying(false);
// 전체 트랙 음소거 복원
tracks.forEach(t => {
wavesurferRefs.current[t.id]?.setMuted(t.muted);
});
}
} else {
if (track.id === trackListRef.current[0].id) {
setIsPlaying(false);
}
}
});
});

return () => {
isMounted = false;
Object.values(wavesurferRefs.current).forEach(ws => ws?.destroy());
};
}, []);

// 전체 동시 재생 / 일시정지
const handleMasterPlayPause = () => {
// 순차 재생 중이었다면 중지
if (isSequentialRef.current) {
isSequentialRef.current = false;
setIsSequentialPlaying(false);
trackList.forEach(t => {
wavesurferRefs.current[t.id]?.pause();
wavesurferRefs.current[t.id]?.setMuted(t.muted);
});
}

const nextState = !isPlaying;
setIsPlaying(nextState);

Object.values(wavesurferRefs.current).forEach(ws => {
if (ws) {
if (nextState) ws.play();
else ws.pause();
}
});
};

// 🔁 스템별 순차적 솔로 재생 시작/중지
const handleSequentialPlay = () => {
if (isPlaying) {
// 동시 재생 중이면 먼저 중지
Object.values(wavesurferRefs.current).forEach(ws => ws?.pause());
setIsPlaying(false);
}

const nextSequentialState = !isSequentialPlaying;
isSequentialRef.current = nextSequentialState;
setIsSequentialPlaying(nextSequentialState);

if (nextSequentialState) {
sequentialIndexRef.current = 0;
trackList.forEach((t, idx) => {
const ws = wavesurferRefs.current[t.id];
if (ws) {
ws.setTime(0);
if (idx === 0) {
ws.setMuted(false);
ws.play();
} else {
ws.setMuted(true); // 첫 번째 트랙 외에는 모두 음소거하고 순서대로 재생
ws.pause();
}
}
});
} else {
// 순차 재생 취소 시 모든 트랙 일시정지 및 원래 음소거 상태 복원
trackList.forEach(t => {
const ws = wavesurferRefs.current[t.id];
if (ws) {
ws.pause();
ws.setMuted(t.muted);
}
});
}
};

// 개별 트랙 음소거 토글
const handleToggleMute = (trackId) => {
setTrackList(prev => prev.map(t => {
if (t.id === trackId) {
const newMuted = !t.muted;
const ws = wavesurferRefs.current[trackId];
if (ws && !isSequentialRef.current) ws.setMuted(newMuted);
return { ...t, muted: newMuted };
}
return t;
}));
};

// 타임스탬프 클릭 시 위치 이동
const handleSeek = (seconds) => {
Object.values(wavesurferRefs.current).forEach(ws => {
if (ws) ws.setTime(seconds);
});
setCurrentTime(seconds);
};

const handleCommentInputChange = (trackId, text) => {
setTrackList(prev => prev.map(t => {
if (t.id === trackId) return { ...t, newCommentText: text };
return t;
}));
};

const handleAddComment = (trackId, e) => {
e.preventDefault();
setTrackList(prev => prev.map(t => {
if (t.id === trackId) {
if (!t.newCommentText.trim()) return t;
const newComment = {
id: Date.now(),
author: '나 (아티스트)',
timestamp_seconds: Number(currentTime.toFixed(2)),
text: t.newCommentText
};
return {
...t,
comments: [...t.comments, newComment].sort((a, b) => a.timestamp_seconds - b.timestamp_seconds),
newCommentText: ''
};
}
return t;
}));
};

const formatTime = (secs) => {
const m = Math.floor(secs / 60);
const s = Math.floor(secs % 60);
return `${m}:${s < 10 ? '0' : ''}${s}`;
};

return (
<div style={{ maxWidth: '720px', margin: '40px auto', padding: '28px', background: '#fff', borderRadius: '16px', boxShadow: '0 4px 16px rgba(0,0,0,0.06)', fontFamily: 'sans-serif' }}>
<h2 style={{ fontSize: '22px', fontWeight: 'bold', marginBottom: '4px' }}>멀티트랙 개별 피드백 스튜디오</h2>
<p style={{ fontSize: '14px', color: '#666', marginBottom: '24px' }}>동시 재생 또는 스템별 순차적 솔로 재생으로 각각의 사운드를 세밀하게 검토하세요.</p>

{/* 플레이어 컨트롤 바 (동시 재생 및 순차 재생 버튼) */}
<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px', padding: '14px 18px', background: '#f8fafc', borderRadius: '12px', border: '1px solid #e2e8f0', gap: '10px', flexWrap: 'wrap' }}>
<div style={{ display: 'flex', gap: '8px' }}>
<button
onClick={handleMasterPlayPause}
style={{ padding: '10px 16px', background: isPlaying ? '#ef4444' : '#6366f1', color: '#fff', border: 'none', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold', fontSize: '14px' }}
>
{isPlaying ? '⏸ 전체 일시정지' : '▶ 전체 동시 재생'}
</button>
<button
onClick={handleSequentialPlay}
style={{ padding: '10px 16px', background: isSequentialPlaying ? '#d97706' : '#0f172a', color: '#fff', border: 'none', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold', fontSize: '14px' }}
>
{isSequentialPlaying ? '⏹ 순차 재생 중지' : '🔁 스템별 순차 재생'}
</button>
</div>
<span style={{ fontFamily: 'monospace', fontSize: '15px', fontWeight: 'bold', color: '#333' }}>
{formatTime(currentTime)} / {formatTime(duration)}
</span>
</div>

{/* 멀티트랙 스템 목록 */}
<div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
{trackList.map((track, idx) => (
<div
key={track.id}
style={{
padding: '16px',
background: isSequentialPlaying && sequentialIndexRef.current === idx ? '#eff6ff' : '#fafafa',
borderRadius: '12px',
border: isSequentialPlaying && sequentialIndexRef.current === idx ? '2px solid #3b82f6' : '1px solid #e5e7eb',
transition: 'all 0.2s'
}}
>
<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
<div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
<span style={{ fontSize: '15px', fontWeight: 'bold', color: '#111' }}>{track.title}</span>
{isSequentialPlaying && sequentialIndexRef.current === idx && (
<span style={{ padding: '2px 6px', background: '#3b82f6', color: '#fff', fontSize: '11px', fontWeight: 'bold', borderRadius: '4px' }}>
재생 중 🎵
</span>
)}
</div>
<button
onClick={() => handleToggleMute(track.id)}
style={{
padding: '4px 10px',
background: track.muted ? '#ef4444' : '#e5e7eb',
color: track.muted ? '#fff' : '#374151',
border: 'none',
borderRadius: '6px',
fontSize: '12px',
cursor: 'pointer',
fontWeight: 'bold'
}}
>
{track.muted ? '🔇 음소거 해제' : '🔊 음소거'}
</button>
</div>

{/* 웨이브폼 */}
<div
ref={(el) => (containerRefs.current[track.id] = el)}
style={{ width: '100%', background: '#fff', borderRadius: '6px', overflow: 'hidden', marginBottom: '12px' }}
/>

{/* 댓글 입력 폼 */}
<form onSubmit={(e) => handleAddComment(track.id, e)} style={{ display: 'flex', gap: '8px', marginBottom: '12px' }}>
<input
type="text"
value={track.newCommentText}
onChange={(e) => handleCommentInputChange(track.id, e.target.value)}
placeholder={`이 트랙의 현재 위치(${formatTime(currentTime)})에 피드백 남기기...`}
style={{ flex: 1, padding: '8px 12px', border: '1px solid #ddd', borderRadius: '6px', outline: 'none', fontSize: '13px' }}
/>
<button
type="submit"
style={{ padding: '8px 14px', background: '#334155', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontSize: '13px', fontWeight: 'bold' }}
>
등록
</button>
</form>

{/* 피드백 목록 */}
{track.comments.length > 0 && (
<div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
<div style={{ fontSize: '12px', fontWeight: 'bold', color: '#64748b' }}>이 트랙의 피드백 ({track.comments.length})</div>
<div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '140px', overflowY: 'auto' }}>
{track.comments.map((c) => (
<div
key={c.id}
onClick={() => handleSeek(Number(c.timestamp_seconds))}
style={{ padding: '8px 10px', background: '#fff', borderRadius: '6px', cursor: 'pointer', border: '1px solid #e2e8f0', transition: 'background 0.2s' }}
>
<div style={{ display: 'flex', alignItems: 'center', marginBottom: '2px' }}>
<span style={{ display: 'inline-block', padding: '1px 5px', background: '#e0e7ff', color: '#4338ca', fontSize: '11px', fontWeight: 'bold', borderRadius: '4px', marginRight: '6px' }}>
{formatTime(Number(c.timestamp_seconds))}
</span>
<span style={{ fontSize: '11px', fontWeight: 'bold', color: '#333' }}>{c.author}</span>
</div>
<p style={{ fontSize: '13px', color: '#475569', margin: 0 }}>{c.text}</p>
</div>
))}
</div>
</div>
)}
</div>
))}
</div>
</div>
);
}
