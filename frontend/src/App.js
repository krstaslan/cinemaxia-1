import { Container } from 'react-bootstrap'
import React from 'react';
import {BrowserRouter as Router ,Route} from 'react-router-dom'
import HomeScreen from './screens/HomeScreen'
import MovieScreen from './screens/MovieScreen'
import Header from './components/Header'
import Footer from './components/Footer'
function App() {
  return (
    <Router>
      <Header/>
      <main className='py-5'>
        <Container>
        {/* <Route path="/movie/" component={MovieScreen}  />  */}
        {/* <Route path="/" component={HomeScreen} exact /> */}
        </Container>
        
      <HomeScreen />  
      </main>
      <Footer/>
    </Router>
  );
}

export default App;
