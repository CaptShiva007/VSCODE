<?php
// Database connection
$servername = "localhost";
$username = "theju01";
$password = "pass";
$dbname = "achievement_tracker";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $eventName = $_POST["event-name"];
    $date = $_POST["date"];
    $category = $_POST["category"];

    // Insert data into database
    $sql = "INSERT INTO achievements (event_name, date, category) VALUES ('$eventName', '$date', '$category')";
    if ($conn->query($sql) === TRUE) {
        echo "Achievement added successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Close database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard | Achievement Tracker</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <header>
        <h1>Achievement Tracker</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Logout</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section class="dashboard-section">
            <h2>My Dashboard</h2>
            
            <!-- Form to update achievements -->
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST">
                <div class="form-group">
                    <label for="event-name">Event Name</label>
                    <input type="text" id="event-name" name="event-name" required>
                </div>
                <div class="form-group">
                    <label for="date">Date</label>
                    <input type="date" id="date" name="date" required>
                </div>
                <div class="form-group">
                    <label for="category">Category</label>
                    <select id="category" name="category">
                        <option value="Fitness">Fitness</option>
                        <option value="Education">Education</option>
                        <option value="Career">Career</option>
                        <option value="Personal Development">Personal Development</option>
                        <!-- Add more categories as needed -->
                    </select>
                </div>
                <button type="submit" class="submit-button">Update Achievement</button>
            </form>
            
            <!-- Display current achievements -->
            <div class="achievements-list">
                <h3>My Achievements</h3>
                <ul>
                    <!-- Fetch achievements from database and display them here -->
                    <?php
                    $sql = "SELECT * FROM achievements";
                    $result = $conn->query($sql);

                    if ($result->num_rows > 0) {
                        while($row = $result->fetch_assoc()) {
                            echo "<li><strong>Event:</strong> " . $row["event_name"] . "<br>";
                            echo "<strong>Date:</strong> " . $row["date"] . "<br>";
                            echo "<strong>Category:</strong> " . $row["category"] . "</li>";
                        }
                    } else {
                        echo "No achievements yet";
                    }
                    ?>
                </ul>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Achievement Tracker. All rights reserved.</p>
    </footer>
</body>
</html>
