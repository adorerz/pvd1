from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SpiritualRecord, User


from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

    # List of Major World Religions
    RELIGION_CHOICES = [
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Judaism', 'Judaism'),
        ('Sikhism', 'Sikhism'),
        ('Shinto', 'Shinto'),
        ('Taoism', 'Taoism'),
        ('Baháʼí Faith', 'Baháʼí Faith'),
        ('Jainism', 'Jainism'),
        ('Zoroastrianism', 'Zoroastrianism'),
        ('Other', 'Other'),
    ]
    
    religion = forms.ChoiceField(choices=RELIGION_CHOICES)

    # List of All Countries in the World
    COUNTRY_CHOICES = [
        ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'),
        ('Angola', 'Angola'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'),
        ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'),
        ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'),
        ('Cabo Verde', 'Cabo Verde'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'),
        ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'),
        ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo (Congo-Brazzaville)', 'Congo (Congo-Brazzaville)'),
        ('Congo (Congo-Kinshasa)', 'Congo (Congo-Kinshasa)'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czechia', 'Czechia'), ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'),
        ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'),
        ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'),
        ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'),
        ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'),
        ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'),
        ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'),
        ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('North Korea', 'North Korea'), ('Norway', 'Norway'),
        ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palestine', 'Palestine'), ('Panama', 'Panama'),
        ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'),
        ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Romania', 'Romania'), ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'),
        ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('South Africa', 'South Africa'),
        ('South Korea', 'South Korea'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'),
        ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'),
        ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'),
        ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'),
        ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe'),
        ('Other', 'Other'),
    ]
    
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'religion', 'country', 'password1', 'password2']



from django import forms
from .models import SpiritualRecord, User

class SpiritualRecordForm(forms.ModelForm):
    class Meta:
        model = SpiritualRecord
        fields = ['record_type', 'text', 'audio']  



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile_photo']
