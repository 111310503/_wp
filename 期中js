<!DOCTYPE html>
    <style>
        #movingButton {
            position: absolute;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            transition: transform 0.5s;
        }
    </style>

<body>
    <h1 id="scoreTitle">分數: 0</h1>
    <button id="movingButton">click</button>

    <script>
        const button = document.getElementById('movingButton');
        const scoreTitle = document.getElementById('scoreTitle');
        let score = 0;

        function moveButton() {
            const x = Math.random() * (window.innerWidth - button.offsetWidth);
            const y = Math.random() * (window.innerHeight - button.offsetHeight);
            button.style.transform = `translate(${x}px, ${y}px)`;
        }
        function updateScore() {
            score++;
            button.textContent = `click`;
            scoreTitle.textContent = `分數: ${score}`;
          
             if (moveInterval > 0) { 
                moveInterval -= 50;
                clearInterval(moveIntervalId);
                moveIntervalId = setInterval(moveButton, moveInterval);
            }

        }

        function updateScore() {
            score++;
            button.textContent = `click`;
            scoreTitle.textContent = `分數: ${score}`;
    }

        button.addEventListener('click', () => {
            button.style.display = 'none';
            setTimeout(() => {
                button.style.display = 'block';
                moveButton();}, 3000); 
            updateScore();
        });

        // Initial button position
        moveButton();

        // Continuously move button every second
        setInterval(moveButton, 1000);
    </script>
</body>
</html>
