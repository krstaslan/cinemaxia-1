import React from 'react'
import {Link} from 'react-router-dom'
import { Row, Col, Image,ListGroup,Button,Card  } from 'react-bootstrap'
import { ListGroupItem } from 'react-bootstrap'

function MovieScreen() {
  const movie= "Top Gun ";
  const column=4;
  return (
    <div>
      <Link to="/" className='btn btn-light my-3'>Go Back</Link>
      <Row>
        <Col md={6}>
          <Image src={movie.image} alt={movie.name} fluit />
        </Col>
        <Col md={3}>
          <ListGroup varinat='flush'>
            <ListGroup.Item>
              <h3>{movie.name}</h3>
            </ListGroup.Item>
            {/* for loop for seats */}
            {/* for (let seat = 0; seat < column; seat++) {
              const element = seat;
              
            }; */}
          </ListGroup>
        </Col>
      </Row>
    </div>
  )
}

export default MovieScreen
