from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    bio = models.CharField(max_length =200)
    profile_pic = models.ImageField(upload_to = 'photos/', default='photos/default.jpg')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length = 12)
    neighbourhood  = models.ForeignKey('Neighbourhood', null=True,related_name='people_count')

    def __str__(self):
        return self.contact

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    @classmethod
    def search_by_username(cls,search_term):
        search_result = cls.objects.filter(user__username__icontains=search_term)
        return search_result


class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True)
    headman=  models.ForeignKey(User, on_delete=models.CASCADE)
    members_count = models.IntegerField(default=0, null=True)
    police_dept = models.CharField(max_length=50)
    police_dept_address = models.CharField(max_length=50)
    health_dept = models.CharField(max_length=50)
    health_dept_address = models.CharField(max_length=50)


    def __str__(self):
        return f' {self.name}'


    @classmethod
    def create_neigborhood(cls):
        cls.save()
    @classmethod
    def delete_neigborhood(cls, id):
        delet = cls.objects.filter(id=id).delete()

    @classmethod
    def find_neigborhood(cls,search_term):
        search_result = cls.objects.filter(bsn_name__icontains=search_term)
        return search_result   
                   
    @classmethod
    def update_neigborhood(cls,id):
        updates = cls.objects.filter(id=id).update()
        return updates

    @classmethod
    def update_occupants(cls,id):
        people = cls.objects.filter(id=id).update()
        return people




class Business(models.Model):
    business_name = models.CharField(max_length=64, unique= True)
    biz_user = models.ForeignKey(User,on_delete=models.CASCADE)
    biz_hood = models.ForeignKey(Neighbourhood, null=True)
    business_email = models.EmailField(max_length=64, unique= True) 
    description = models.TextField(max_length =500)
    descriptive_image = models.ImageField(upload_to = 'photos/', default='photos/default_biz.jpg')

    @classmethod
    def find_biz(cls,search_term):
        search_result = cls.objects.filter(biz_name__icontains=search_term)
        return search_result   
    @classmethod
    def create_business(cls, **kwargs):
        home = Neighbourhood.objects.get(id=request.user.profile.community.id)  
        new_biz = Business(biz_name=biz,biz_user=request.user,biz_hood=home,biz_email=muk@gmail)
        new_biz.save()


    @classmethod
    def delete_business(cls, id):
        to_delete = cls.objects.filter(id=id).delete()

    @classmethod
    def update_biz(cls,id):
        biz = cls.objects.filter(id=id).update()
        return biz

class Post(models.Model):
    post_title =  models.CharField(max_length =20)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name="user_name")
    profile = models.ForeignKey(Profile,null=True)
    text = models.TextField(max_length =500)
    hood  = models.ForeignKey('Neighbourhood', null=True,related_name='post_hood')
    descriptive_picture = models.ImageField(upload_to = 'photos/', default='photos/default_post.jpg')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title