class CommentSerializer(serializers.ModelSerializer):
    blog_title = serializers.CharField(source='blog.title', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'blog', 'blog_title', 'text']
