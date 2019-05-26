from django.test import TestCase
from .models import TechType, ProductTech, TechReview, TechMeeting
from django.urls import reverse

class TesterClass(TestCase):

#TechType tests
    def test_ttresult(self):
        tt = TechType(techtypename = 'IDE Manager')
        self.assertEqual(str(tt), tt.techtypename)
        
    def test_tt(self):
        self.assertEqual(str(TechType._meta.db_table), 'techtype')
        
#ProductTech tests   
    def test_ptresult(self):
        pt = ProductTech(productname = 'USB Carrier')
        self.assertEqual(str(pt), pt.productname)
            
    def test_pt(self):
        self.assertEqual(str(ProductTech._meta.db_table), 'producttech')
    
#TechReview tests
    def test_trresult(self):
        tr = TechReview(reviewtitle = 'Tech review')
        self.assertEqual(str(tr), tr.reviewtitle)
            
    def test_tr(self):
        self.assertEqual(str(TechReview._meta.db_table), 'techreview')
        
#TechMeeting tests
    def test_tmresult(self):
        tm = TechMeeting(meetingtype = 'Django Meeting')
        self.assertEqual(str(tm), tm.meetingtype)
        
    def test_tm(self):
        self.assertEqual(str(TechMeeting._meta.db_table), 'techmeeting')       
        
#View tests
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
class MeetingTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('createmeeting'), follow = True)
        self.assertEqual(response.status_code, 200)     
        
class ResourceTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('createresource'), follow = True)
        self.assertEqual(response.status_code, 200)
    
class FindMeetingTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('findameeting'), follow = True)
        self.assertEqual(response.status_code, 200)
        
class MeetingViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meeting'), follow = True)
        self.assertEqual(response.status_code, 200)
    
class MeetingDetailTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingdetail'), follow = True)
        self.assertEqual(response.status_code, 200)
        
class MeetingResultTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingresult'), follow = True)
        self.assertEqual(response.status_code, 200)
        
class ResourceViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resource'), follow = True)
        self.assertEqual(response.status_code, 200)
        
#Template test        
class TemplateTest(TestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/index.html')