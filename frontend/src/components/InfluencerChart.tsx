// Recharts example
import React from 'react'
import { LineChart, Line, XAxis, YAxis, Tooltip } from 'recharts'

export default function InfluencerChart(){
  const data = [{name:'Day1',eng:0.05},{name:'Day2',eng:0.08}]
  return (
    <LineChart width={600} height={300} data={data}>
      <XAxis dataKey='name'/>
      <YAxis />
      <Tooltip />
      <Line type='monotone' dataKey='eng' stroke='#8884d8' />
    </LineChart>
  )
}
