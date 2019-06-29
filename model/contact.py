from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobile=None, workphone=None, fax=None, email1=None, email2=None,
                 email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                 secaddress=None, phone2=None, notes=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.secaddress = secaddress
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address,
                                                     self.homephone, self.mobile, self.workphone, self.phone2,
                                                     self.email1, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname\
                and self.lastname == other.lastname and self.homephone == other.homephone and \
                self.mobile == other.mobile and self.workphone == other.workphone and self.phone2 == other.phone2 and \
                self.address == other.address and self.email1 == other.email1 and self.email2 == other.email2 and \
                self.email3 == other.email3

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize