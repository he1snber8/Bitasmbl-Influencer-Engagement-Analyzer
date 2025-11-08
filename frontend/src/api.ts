// API client
export async function fetchInfluencer(id:string){
  const r = await fetch(`/api/influencer/${id}`)
  return r.json()
}

export async function search(q:string){
  const r = await fetch(`/api/search?q=${encodeURIComponent(q)}`)
  return r.json()
}
