# Business Requirement Document (BRD)

## Project Objective

Develop a data ingestion solution that can process user information files in multiple formats (`Excel`, `CSV`, and `JSON`), standardize the data into JSON format, and synchronize the records into a MySQL database.

---

# Business Requirements

## 1. File Intake

The system shall accept a file path as input from the user or calling application.

The system shall support the following file formats:

- Excel (`.xlsx`, `.xls`)
- CSV (`.csv`)
- JSON (`.json`)

The system shall identify the file type automatically based on the file extension.

---

## 2. Data Conversion

### Excel / CSV Files

When the input file is an Excel or CSV file:

- The system shall read all records from the file.
- The system shall convert the file content into JSON format.
- The generated JSON data shall be stored in memory for further processing.

### JSON Files

When the input file is a JSON file:

- The system shall read and validate the JSON content.
- The JSON content shall be stored in memory for processing.

---

## 3. User Information Structure

The uploaded data file shall contain user-related information with approximately 10 fields having different data types.

Example business fields may include:

- User ID
- First Name
- Last Name
- Email Address
- Phone Number
- Date of Birth
- Salary
- Active Status
- Created Date
- Department

---

## 4. JSON Archive Requirement

The system shall save the processed JSON data into a dedicated output location.

The output location shall be configurable through environment or application configuration settings.

The generated JSON file name shall follow a timestamp-based naming convention to ensure uniqueness.

Example filename format:

    yyyyMMdd_HHmmss_fff.json

---

## 5. Database Integration

The system shall connect to a MySQL database using a configurable connection string stored in environment settings.

The system shall insert new records and update existing records in the target database table.

---

## 6. Stored Procedure Requirement

Database operations shall be performed using a MySQL Stored Procedure.

The Stored Procedure shall:

- Insert new user records
- Update existing user records when matching keys already exist

The Stored Procedure script shall be maintained separately within the project under a dedicated database scripts folder.

---

## 7. Error Handling

The system shall handle and report the following scenarios:

- Invalid or inaccessible file paths
- Unsupported file formats
- Empty files
- Invalid JSON structure
- Database connection failures
- Database execution errors

Appropriate error messages and logs shall be generated for troubleshooting purposes.

---

## 8. Logging and Audit

The system shall maintain logs for:

- File processing status
- Record count processed
- JSON generation status
- Database synchronization status
- Error and exception details

---

## 9. Security and Configuration

Sensitive information such as database connection strings and output folder paths shall be configurable through environment settings and shall not be hardcoded within the application.

---

## 10. Expected Outcome

The solution shall enable automated ingestion, transformation, archival, and database synchronization of structured user information files while ensuring maintainability, traceability, and scalability.