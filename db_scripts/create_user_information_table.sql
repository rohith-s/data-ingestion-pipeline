CREATE DATABASE IF NOT EXISTS data_ingestion_db;

USE data_ingestion_db;

CREATE TABLE IF NOT EXISTS user_information
(
    user_id INT AUTO_INCREMENT PRIMARY KEY,

    employee_code VARCHAR(20),

    first_name VARCHAR(100) NOT NULL,

    last_name VARCHAR(100) NOT NULL,

    email VARCHAR(255) NOT NULL,

    phone_number VARCHAR(20),

    date_of_birth DATE,

    salary DECIMAL(12,2),

    bonus_percentage FLOAT,

    is_active BOOLEAN DEFAULT TRUE,

    joining_datetime DATETIME,

    last_login_timestamp TIMESTAMP NULL DEFAULT NULL,

    profile_json JSON,

    profile_picture BLOB,

    rating DOUBLE,

    gender ENUM('Male', 'Female', 'Other') NOT NULL,

    created_by VARCHAR(100),

    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_by VARCHAR(100),

    updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

-- Composite index for matching logic
CREATE INDEX idx_user_match
ON user_information
(
    first_name,
    last_name,
    email,
    gender
);

-- Optional employee code index
CREATE INDEX idx_employee_code
ON user_information(employee_code);