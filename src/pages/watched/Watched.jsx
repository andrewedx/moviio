import { useEffect, useState } from 'react';
import MovieContainer from "../../components/MovieContainer";
import searchIcon from "../../search.svg"
import AtomicSpinner from 'atomic-spinner';


const refData = []
const url = "http://127.0.0.1:5000/local"

function getData() {
    fetch("http://127.0.0.1:5000/local")
        .then(response => response.json())
        .then(data => {
            // Data extraction and manipulation
            console.log(data); // Log the received data to the console
            // Perform further operations with the data as needed
        })
        .catch(error => {
            // Handle any errors that occur during the fetch request
            console.error('Error:', error);
        });
}

const Watched = () => {
    const [searchTerm, setSearchTerm] = useState("");
    const [movies, setMovies] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        const abortCont = new AbortController();
        setTimeout(() => {
            fetch(url, {signal: abortCont.signal}).then(res => {
                console.log(res);
                if (!res.ok){
                    throw Error('Could not fetch the data for that resource')
                }
                return res.json();
            }).then(data => {
                console.log(data)
                setMovies(data);
                setLoading(false)
                setError(null)
            }).catch(err => {
                if (err.name === 'AbortError') {console.log("Fetch Aborted")}
                else{
                    setError(err.message)
                    setLoading(false)
                }
            })
        }, 1000);

        return () => abortCont.abort();
    }, [url]);
    

    return ( 
        <div className="app">
            <h1>Watched</h1>

            <div className="search">
                <input
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    placeholder="Search Your Watched Movies"
                />
                <img
                    src={searchIcon}
                    alt="search"
                    onClick={() => getData()}
                />
            </div>

            {error && <div>{error}</div>} 
            {loading && <div><AtomicSpinner /></div>}
            {loading && <div>Loading...</div>}
            {movies && <MovieContainer movies={movies}/>}
    
        </div>
     );
}
 
export default Watched;