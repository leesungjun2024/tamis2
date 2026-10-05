import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://your_project_id.supabase.co'
const supabaseKey = "krsungjun@gmail.com's Project"

// Supabase가 설정되었는지 확인하는 플래그
const isConfigured = !supabaseUrl.includes('https://eahxnlgjzbxoxooxdxeg.supabase.co')

// 설정되지 않은 경우 네트워크 요청을 보내지 않고 로컬 모드로 안전하게 동작하는 가짜(Mock) 클라이언트 제공
export const supabase = isConfigured
? createClient(supabaseUrl, supabaseKey)
: {
from: () => ({
select: () => ({
eq: () => ({
order: () => Promise.resolve({ data: [], error: null })
})
}),
insert: () => ({
select: () => Promise.resolve({ data: [], error: null })
})
})
};
