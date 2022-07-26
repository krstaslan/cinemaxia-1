import { Row, Col } from 'react-bootstrap'
import React from 'react'
import Movie from '../components/Movie'

function HomeScreen() {
  return (
    <div>
      <h1>
        <Row>
            <Col>
            <Movie />
            </Col>
            <Col>
            <Movie />
            </Col>
            <Col>
            <Movie />
            </Col>

        </Row>
      </h1>
    </div>
  )
}
export default HomeScreen;