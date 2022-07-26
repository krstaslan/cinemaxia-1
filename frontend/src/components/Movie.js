import React from 'react'
import {Card } from 'react-bootstrap'
import { Link } from 'react-router-dom'


function Movie({movie}) {
  return (
    <Card className='my-3 p-3 rounded '>
     <Link to={'/movie/${movie.id}'}>
     </Link>
    </Card>
  )
}
export default Movie;