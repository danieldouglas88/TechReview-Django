from django.test import TestCase
from .models import TechType, ProductTech, TechReview, TechMeeting

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