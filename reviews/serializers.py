from rest_flex_fields import FlexFieldsModelSerializer
from .models import Product, Category, Company, ProductSize, ProductSite, Comment, Image
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class CompanySerializer(FlexFieldsModelSerializer):
	class Meta:
		model = Company
		fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
	class Meta:
		model = Category
		fields = ['pk', 'name']
		expandable_fields = {
		  'products': ('reviews.ProductSerializer', {'many': True})
		}


class ProductSizeSerializer(FlexFieldsModelSerializer):
	class Meta:
		model = ProductSize
		fields = ['pk', 'name']



# Application definition
# class ProductSerializer(serializers.ModelSerializer):
# 	category = CategorySerializer(many=True)

# 	class Meta:
# 		model = Product
		# fields = ['pk', 'name', 'category']

class ProductSerializer(FlexFieldsModelSerializer):
	class Meta:
		model = Product
		fields = ['pk', 'name', 'content', 'created', 'updated']
		expandable_fields = {
			'category': ('reviews.CategorySerializer', {'many': True}),
			'sites': ('reviews.ProductSiteSerializer', {'many': True}),
			'comments': ('reviews.CommentSerializer', {'many': True}),
		}
# if you want to include spesific fields, do ?fields=pk,name:
# if you want to leave out the content field, do ?omit=content:
# if you want to expand nested relations, do ?expand=category:
# only product name and category name ?expand=category&fields=name,category.name



class ProductSerializer(FlexFieldsModelSerializer):
	class Meta:
		model = Product
		fields = ['pk', 'name', 'content', 'created', 'updated']
		expandable_fields = {
			'category': ('reviews.CategorySerializer', {'many': True}),
			'sites': ('reviews.ProductSiteSerializer', {'many': True}),
			'comments': ('reviews.CommentSerializer', {'many': True}),
			'image': ('reviews.ImageSerializer', {'many': True}),
		}


class UserSerializer(FlexFieldsModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
	class Meta:
		model = Comment
		fields = ['pk', 'title', 'content', 'created', 'updated']
		expandable_fields = {
			'product': 'reviews.CategorySerializer',
			'user': 'reviews.UserSerializer'
		}


# If we need a product response with category, comments and sites (with product size and company) and we dont need a product content field. we can do :
# /product/1/?expand=category,comments,sites.company,sites.productsize&omit=content


class ImageSerializer(FlexFieldsModelSerializer):
	image = VersatileImageFieldSerializer(
		sizes='product_headshot'
	)

	class Meta:
		model = Image
		fields = ['pk', 'name', 'image']
# Navigate to product/1/?expand=image&omit=content. You should see images in serialized data.

