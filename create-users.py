#!/usr/bin/env python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        # Check if the line starts with a # using regular expression.
        # Lines starting with # are treated as comments and should be ignored.
        match = re.match('^#', line)

        # Strip any whitespace from the line and split it into parts based on ':'.
        # This is expected for a line format resembling: username:password:firstname:lastname:groups
        fields = line.strip().split(':')

        # Check if the line is a comment or does not contain exactly 5 fields.
        # We need exactly 5 fields for a valid user account configuration.
        if match or len(fields) != 5:
            continue

        # Extract user information from the fields
        username = fields[0]
        password = fields[1]
        # The GECOS field is used to store user information like full name, room number, phone, etc.
        # Here, it's formatted to include first and last name, leaving other fields empty.
        gecos = "%s %s,,," % (fields[3], fields[2])
        # Split the groups field into a list, as users can belong to multiple groups.
        groups = fields[4].split(',')

        # Inform about the user account creation process and construct the command for adding the user.
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        # Execute the command to create the user account without a password.
        os.system(cmd)
        print(f"==> Setting the password for {username}...")
        # Set the user's password by piping it into the passwd command using echo.
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        os.system(cmd)
        # Assign the user to specified groups, skipping any '-' placeholders.
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                os.system(cmd)

if __name__ == '__main__':
    main()

