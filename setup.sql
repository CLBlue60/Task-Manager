--Create database table
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64),
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

-- Create some dummy data to test with:
INSERT INTO tasks (
    name,
    summary,
    description
) VALUES
(
    "John",
    "Walk the dog",
    "Make sure it's at least 3 laps"
),
(
    "Jane",
    "Buy groceries",
    "Don't forget the milk and eggs"
),
(
    "Bob",
    "Clean the house",
    "Vacuum, dust, and mop the floors"
);
