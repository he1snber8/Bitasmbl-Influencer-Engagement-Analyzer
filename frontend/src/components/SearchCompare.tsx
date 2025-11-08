// Search and compare UI
import React, {useState} from 'react'

export default function SearchCompare(){
  const [q,setQ]=useState('')
  return (
    <div>
      <input value={q} onChange={e=>setQ(e.target.value)} placeholder='Search influencer' />
      <button>Search</button>
    </div>
  )
}
