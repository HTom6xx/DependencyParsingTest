### Summary
- Dependency analysis test with GiNZA.
- The analysis results are visualized as an HTML document using pyvis.
- Offline operation is possible after container startup or when there is a build cache.

### Prerequisites
- Windows 11 Pro
- Connected to the internet
- Web browser available
    - Google Chrome
    - Microsoft Edge
- ```docker compose``` command is available

### Getting Started
1. Execute one of the following
    - Running command
        ```bash
        docker compose -f docker/docker-compose.yml up
        ```
    - Running command
        ```
        execute.bat
        ```

1. Access via web browser
    - [```http://localhost:8080/```](http://localhost:8080/)

1. Enter a Japanese sentence in the ```元文章：``` field.
1. Click the ```実行``` button to run the dependency analysis.
    - The results will be saved in ````data/cache/*.html``` directly under the project folder.
    - A download link will be added to the bottom of the page shortly.