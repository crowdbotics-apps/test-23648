from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CategoryViewSet,
    CourseViewSet,
    EnrollmentViewSet,
    EventViewSet,
    GroupViewSet,
    LessonViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    RecordingViewSet,
    SubscriptionViewSet,
    SubscriptionTypeViewSet,
)

router = DefaultRouter()
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("event", EventViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("recording", RecordingViewSet)
router.register("module", ModuleViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("lesson", LessonViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("group", GroupViewSet)
router.register("category", CategoryViewSet)
router.register("course", CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
