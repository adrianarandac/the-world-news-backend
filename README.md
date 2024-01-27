
# The World News Backend

The World News Backend is a FastAPI application designed to scrape and serve the latest news headlines from the WorldNews subreddit. It's built with Python and uses the Beautiful Soup library for scraping, alongside FastAPI for the web framework.

## Features

- Fetch the latest news headlines from the WorldNews subreddit.
- Serve news headlines through a RESTful API.

## Installation and running the server

Install and run the necessary dependencies as listed in the `pyproject.toml` file with:

`poetry install`

`poetry run start`

## API Endpoints

- `GET /news`: Fetch and return the latest news headlines from WorldNews subreddit.

## Authors

- Adrian Aranda - <adrienaranda@gmail.com>

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the creators and maintainers of FastAPI, Beautiful Soup, and Requests for their fantastic libraries that made this project possible.
- Reddit for providing the WorldNews subreddit as a source of news headlines.

## Contributing

Contributions are welcome! Feel free to submit a pull request.

## Support

If you encounter any issues or have any questions about the application, please file an issue on the project's GitHub issue tracker.

This version of the README avoids any specific command instructions or code blocks, while still providing an overview of the project, its features, and how to use it.