
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22],
                "last_name": self.last_name
            }
        ]

    def update_member(self, id, updated_data):
     for member in self._members:
        if member["id"] == id:
            member.update(updated_data)
            return member
     return None
    


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if "id" not in member:
         member["id"] = self._generateId()

        member["last_name"] = self.last_name
        self._members.append(member)
        return member


    def delete_member(self, id):
       for member in self._members:
         if member["id"] == id:
            self._members.remove(member)
            return True  # Successfully deleted
       return False  # Member not found


    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
               return member
    # If no match found
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    
def update_member(self, id, updated_info):
    for member in self._members:
        if member["id"] == id:
            member.update(updated_info)
            return member
    return None
