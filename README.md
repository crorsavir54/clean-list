# clean-list

Contacts list cleanup automation

Features:
 - Splits fullname into First and Last Name and writes them in to their respective columns
 - Remove noise from email field

Name splitting:
- Assumes that first word in the field is the first name and the rest will be their last name

Email cleaning:
- Finds a valid email using regex and extracts that value only and replace the field.
- Replance emails ending with ".con" with ".com". If .con is not in the end of the email, it will not be able to modify it
