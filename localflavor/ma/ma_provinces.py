# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from localflavor.stub import _

#: An alphabetical list of provinces for use as `choices` in a formfield.
#: http://www.pncl.gov.ma/fr/Pages/decoupage.aspx
PROVINCE_CHOICES_PER_REGION = (
    ('01', _('Al Hoceima'), '01'),
    ('02', _('Larache'), '01'),
    ('03', _('M’Diq - Fnideq'), '01'),
    ('04', _('Tetouan'), '01'),
    ('05', _('Chefchaouene'), '01'),
    ('06', _('Tanger - Assilah'), '01'),
    ('07', _('Fahs - Anjra'), '01'),
    ('08', _('Ouezzane'), '01'),
    ('09', _('Driouch'), '02'),
    ('10', _('Nador'), '02'),
    ('11', _('Berkan'), '02'),
    ('12', _('Taourirt'), '02'),
    ('13', _('Jerada'), '02'),
    ('14', _('Guercif'), '02'),
    ('15', _('Feguig'), '02'),
    ('16', _('Oujda - Angad'), '02'),
    ('17', _('El Hajeb'), '03'),
    ('18', _('Ifrane'), '03'),
    ('19', _('Boulemane'), '03'),
    ('20', _('Taza'), '03'),
    ('21', _('Taounate'), '03'),
    ('22', _('Sefrou'), '03'),
    ('23', _('Fès'), '03'),
    ('24', _('Meknès'), '03'),
    ('25', _('Moulay Yacoub'), '03'),
    ('26', _('Khémisset'), '04'),
    ('27', _('Rabat'), '04'),
    ('28', _('Skhirate - Temara'), '04'),
    ('29', _('Kénitra'), '04'),
    ('30', _('Salé'), '04'),
    ('31', _('Sidi Slimane'), '04'),
    ('32', _('Sidi Kacem'), '04'),
    ('33', _('Casablanca'), '05'),
    ('34', _('Mohamedia'), '05'),
    ('35', _('Nouaceur'), '05'),
    ('36', _('Mediouna'), '05'),
    ('37', _('Benslimane'), '05'),
    ('38', _('Berrachid'), '05'),
    ('39', _('El Jadida'), '05'),
    ('40', _('Sidi Bennour'), '05'),
    ('41', _('Settat'), '05'),
    ('42', _('Azilal'), '06'),
    ('43', _('Fquih Ben Saleh'), '06'),
    ('44', _('Beni Mellal'), '06'),
    ('45', _('Khouribga'), '06'),
    ('46', _('Khénifra'), '06'),
    ('47', _('Safi'), '07'),
    ('48', _('Al Haouz'), '07'),
    ('49', _('Rhamna'), '07'),
    ('50', _('Essaouira'), '07'),
    ('51', _('Youssoufia'), '07'),
    ('52', _('Marrakech'), '07'),
    ('53', _('Chichaoua'), '07'),
    ('54', _('El Kelaa Des Sraghna'), '07'),
    ('55', _('Agadir - Idda Outanane'), '08'),
    ('56', _('Inezgane - Ait Melloul'), '08'),
    ('57', _('Chtouka - Ait Baha'), '08'),
    ('58', _('Tiznit'), '08'),
    ('59', _('Tata'), '08'),
    ('60', _('Taroudant'), '08'),
    ('61', _('Errachidia'), '09'),
    ('62', _('Tinghir'), '09'),
    ('63', _('Zagoura'), '09'),
    ('64', _('Midelt'), '09'),
    ('65', _('Ouarzazate'), '09'),
    ('66', _('Es -Semara'), '12'),
    ('67', _('Laayoune'), '12'),
    ('68', _('Boujdour'), '12'),
    ('69', _('Terfaya'), '12'),
    ('70', _('Aousserd'), '10'),
    ('71', _('Oued Eddahab'), '10'),
    ('72', _('Assa - Zag'), '11'),
    ('73', _('Sidi Ifni'), '11'),
    ('74', _('Tantan'), '11'),
    ('75', _('Guelmim'), '11'),
)

#: A list of Provinces
PROVINCE_CHOICES = tuple([
    (province[0], '%s - %s' % (province[0], province[1]),)
    for province in PROVINCE_CHOICES_PER_REGION
])
