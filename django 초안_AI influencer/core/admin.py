from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, FeedPost, FeedComment


class UserProfileInline(admin.StackedInline):
    """사용자 프로필 인라인"""
    model = UserProfile
    can_delete = False
    verbose_name_plural = '프로필 정보'
    fields = ('address', 'profile_image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


class CustomUserAdmin(UserAdmin):
    """사용자 관리자 페이지 커스터마이징"""
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')


class FeedCommentInline(admin.TabularInline):
    """피드 댓글 인라인"""
    model = FeedComment
    extra = 0
    fields = ('author', 'content', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(FeedPost)
class FeedPostAdmin(admin.ModelAdmin):
    """피드 포스트 관리자"""
    list_display = ('title', 'content_preview', 'image', 'likes_count', 'comment_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'comment_count')
    inlines = [FeedCommentInline]
    date_hierarchy = 'created_at'

    fieldsets = (
        ('기본 정보', {
            'fields': ('title', 'content', 'image')
        }),
        ('통계', {
            'fields': ('likes_count', 'comment_count', 'created_at'),
            'classes': ('collapse',)
        }),
    )

    def content_preview(self, obj):
        """내용 미리보기"""
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = '내용 미리보기'

    def comment_count(self, obj):
        """댓글 수 표시"""
        return obj.comments.count()
    comment_count.short_description = '댓글 수'

    actions = ['reset_likes', 'delete_all_comments']

    def reset_likes(self, request, queryset):
        """좋아요 수 초기화"""
        updated = queryset.update(likes_count=0)
        self.message_user(request, f'{updated}개 포스트의 좋아요 수가 초기화되었습니다.')
    reset_likes.short_description = '선택된 포스트의 좋아요 수 초기화'

    def delete_all_comments(self, request, queryset):
        """모든 댓글 삭제"""
        total_deleted = 0
        for post in queryset:
            deleted_count = post.comments.count()
            post.comments.all().delete()
            total_deleted += deleted_count
        self.message_user(request, f'{total_deleted}개의 댓글이 삭제되었습니다.')
    delete_all_comments.short_description = '선택된 포스트의 모든 댓글 삭제'


@admin.register(FeedComment)
class FeedCommentAdmin(admin.ModelAdmin):
    """피드 댓글 관리자"""
    list_display = ('post_title', 'author', 'content_preview', 'created_at')
    list_filter = ('created_at', 'post', 'author')
    search_fields = ('content', 'author__username', 'post__title')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20

    fieldsets = (
        ('댓글 정보', {
            'fields': ('post', 'author', 'content')
        }),
        ('메타데이터', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def post_title(self, obj):
        """포스트 제목 표시"""
        return obj.post.title
    post_title.short_description = '포스트'
    post_title.admin_order_field = 'post__title'

    def content_preview(self, obj):
        """댓글 내용 미리보기"""
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = '댓글 내용'

    actions = ['delete_selected_comments']

    def delete_selected_comments(self, request, queryset):
        """선택된 댓글들 삭제"""
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f'{count}개의 댓글이 삭제되었습니다.')
    delete_selected_comments.short_description = '선택된 댓글들 삭제'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """사용자 프로필 관리자"""
    list_display = ('user', 'address_preview', 'has_profile_image', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'address')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('사용자 정보', {
            'fields': ('user',)
        }),
        ('프로필 정보', {
            'fields': ('address', 'profile_image')
        }),
        ('메타데이터', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def address_preview(self, obj):
        """주소 미리보기"""
        if obj.address:
            return obj.address[:30] + '...' if len(obj.address) > 30 else obj.address
        return '-'
    address_preview.short_description = '주소'

    def has_profile_image(self, obj):
        """프로필 이미지 여부"""
        return bool(obj.profile_image)
    has_profile_image.boolean = True
    has_profile_image.short_description = '프로필 이미지'


# 기본 User 모델을 언등록하고 커스텀 UserAdmin 등록
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Admin 사이트 헤더 커스터마이징
admin.site.site_header = "SERA AI 인플루언서 관리자"
admin.site.site_title = "SERA Admin"
admin.site.index_title = "SERA 관리 대시보드"
