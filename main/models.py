# main/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)

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

    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES, null=True, blank=True)

    # List of All Countries in the World
    COUNTRY_CHOICES = [
        ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'),
        ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'),
        ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'),
        ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cabo Verde', 'Cabo Verde'),
        ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'),
        ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'),
        ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'),
        ('Congo (Congo-Brazzaville)', 'Congo (Congo-Brazzaville)'),
        ('Congo (Congo-Kinshasa)', 'Congo (Congo-Kinshasa)'), ('Costa Rica', 'Costa Rica'),
        ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czechia', 'Czechia'),
        ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'),
        ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'),
        ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'),
        ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'),
        ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'),
        ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'),
        ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'),
        ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'),
        ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'), ('North Korea', 'North Korea'), ('Norway', 'Norway'),
        ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palestine', 'Palestine'), ('Panama', 'Panama'),
        ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'),
        ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Romania', 'Romania'), ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'),
        ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'),
        ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'),
        ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'),
        ('United Kingdom', 'United Kingdom'), ('United States', 'United States'),
        ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'), ('Other', 'Other'),
    ]

    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    language_preference = models.CharField(
        max_length=10,
        choices=[('en', 'English'), ('es', 'Spanish'), ('fr', 'French')],
        default='en'
    )

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(null=True, blank=True)
    spiritual_affiliation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class SpiritualRecord(models.Model):
    """
    A user’s dream/vision/prophecy record. If is_shared=True,
    it appears on the community page. Users can like, comment, 
    and interpret a shared record.
    """
    RECORD_TYPES = [
        ('dream', 'Dream'),
        ('vision', 'Vision'),
        ('prophecy', 'Prophecy'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=10, choices=RECORD_TYPES)
    text = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to="audio/", null=True, blank=True)
    interpretation = models.TextField(null=True, blank=True)
    is_shared = models.BooleanField(default=False)
    likes = models.PositiveIntegerField(default=0)  # For "likes" from community
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        date_str = self.created_at.strftime('%Y-%m-%d')
        return f"{self.record_type.capitalize()} by {self.user.username} - {date_str}"


class RecordComment(models.Model):
    """
    Comments attached to a shared SpiritualRecord.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    record = models.ForeignKey(
        SpiritualRecord,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        date_str = self.created_at.strftime('%Y-%m-%d')
        return f"Comment by {self.user.username} - {date_str}"


class RecordInterpretation(models.Model):
    """
    Interpretations attached to a shared SpiritualRecord.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    record = models.ForeignKey(
        SpiritualRecord,
        on_delete=models.CASCADE,
        related_name='interpretations'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        date_str = self.created_at.strftime('%Y-%m-%d')
        return f"Interpretation by {self.user.username} - {date_str}"


class CommunityPost(models.Model):
    """
    A general community post (like a blog entry or forum post).
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)  # For "likes"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}: {self.title}"


class CommunityComment(models.Model):
    """
    Comments on a general community post.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(
        CommunityPost,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        date_str = self.created_at.strftime('%Y-%m-%d')
        return f"Comment by {self.user.username} on {self.post.title} ({date_str})"
