USE data_ingestion_db;

DROP PROCEDURE IF EXISTS sp_upsert_user_information;

DELIMITER $$

CREATE PROCEDURE sp_upsert_user_information
(
    IN p_employee_code VARCHAR(20),

    IN p_first_name VARCHAR(100),

    IN p_last_name VARCHAR(100),

    IN p_email VARCHAR(255),

    IN p_phone_number VARCHAR(20),

    IN p_date_of_birth DATE,

    IN p_salary DECIMAL(12,2),

    IN p_bonus_percentage FLOAT,

    IN p_is_active BOOLEAN,

    IN p_joining_datetime DATETIME,

    IN p_last_login_timestamp TIMESTAMP,

    IN p_profile_json JSON,

    IN p_profile_picture BLOB,

    IN p_rating DOUBLE,

    IN p_gender ENUM('Male', 'Female', 'Other'),

    IN p_created_by VARCHAR(100),

    IN p_updated_by VARCHAR(100)
)
BEGIN

    DECLARE v_existing_user_id INT;

    /*
        ============================================
        Mandatory Field Validations
        ============================================
    */

    IF p_first_name IS NULL OR TRIM(p_first_name) = '' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'First Name is mandatory';
    END IF;

    IF p_last_name IS NULL OR TRIM(p_last_name) = '' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Last Name is mandatory';
    END IF;

    IF p_email IS NULL OR TRIM(p_email) = '' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Email is mandatory';
    END IF;

    IF p_gender IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Gender is mandatory';
    END IF;

    /*
        ============================================
        Match Existing Record
        ============================================
    */

    SET v_existing_user_id = NULL;

    -- Match using employee_code first
    IF p_employee_code IS NOT NULL
       AND TRIM(p_employee_code) <> ''
    THEN

        SELECT user_id
        INTO v_existing_user_id
        FROM user_information
        WHERE employee_code = p_employee_code
        LIMIT 1;

    END IF;

    -- Match using business fields if employee_code not found
    IF v_existing_user_id IS NULL THEN

        SELECT user_id
        INTO v_existing_user_id
        FROM user_information
        WHERE first_name = p_first_name
          AND last_name = p_last_name
          AND email = p_email
          AND gender = p_gender
        LIMIT 1;

    END IF;

    /*
        ============================================
        UPDATE Existing Record
        ============================================
    */

    IF v_existing_user_id IS NOT NULL THEN

        UPDATE user_information
        SET
            employee_code = p_employee_code,
            first_name = p_first_name,
            last_name = p_last_name,
            email = p_email,
            phone_number = p_phone_number,
            date_of_birth = p_date_of_birth,
            salary = p_salary,
            bonus_percentage = p_bonus_percentage,
            is_active = p_is_active,
            joining_datetime = p_joining_datetime,
            last_login_timestamp = p_last_login_timestamp,
            profile_json = p_profile_json,
            profile_picture = p_profile_picture,
            rating = p_rating,
            gender = p_gender,
            updated_by = p_updated_by,
            updated_date = NOW()
        WHERE user_id = v_existing_user_id;

    /*
        ============================================
        INSERT New Record
        ============================================
    */

    ELSE

        INSERT INTO user_information
        (
            employee_code,
            first_name,
            last_name,
            email,
            phone_number,
            date_of_birth,
            salary,
            bonus_percentage,
            is_active,
            joining_datetime,
            last_login_timestamp,
            profile_json,
            profile_picture,
            rating,
            gender,
            created_by,
            created_date,
            updated_by,
            updated_date
        )
        VALUES
        (
            p_employee_code,
            p_first_name,
            p_last_name,
            p_email,
            p_phone_number,
            p_date_of_birth,
            p_salary,
            p_bonus_percentage,
            p_is_active,
            p_joining_datetime,
            p_last_login_timestamp,
            p_profile_json,
            p_profile_picture,
            p_rating,
            p_gender,
            p_created_by,
            NOW(),
            p_updated_by,
            NOW()
        );

    END IF;

END$$

DELIMITER ;