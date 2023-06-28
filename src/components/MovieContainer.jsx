import MovieCard from "./MovieCard";


const MovieContainer = ({movies}) => {
    return ( 
        <div className="movie-container">
            {movies?.length > 0 ? (
                <div className="container">
                {movies.map((movie) => (
                    <MovieCard movie={movie} key={movie.imdbID}/>
                ))}
                </div>
            ) : (
                <div className="empty">
                    <h2>No movies found</h2>
                </div>
            )}
        </div>
     );
}
 
export default MovieContainer;