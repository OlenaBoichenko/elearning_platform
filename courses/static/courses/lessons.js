document.addEventListener('DOMContentLoaded', function () {
    // Handler for going to a lesson when a link is clicked
    const lessonLinks = document.querySelectorAll('.lesson-link');
    if (lessonLinks.length > 0) {
        lessonLinks.forEach(link => {
            link.addEventListener('click', function (event) {
                event.preventDefault();
                const lessonId = this.dataset.lessonId;
                const courseId = this.dataset.courseId;

                if (courseId && lessonId) {
                    window.location.href = `/course/${courseId}/lesson/${lessonId}/`;
                } 
            });
        });
    } else {
        console.log('Lesson links not found, possibly not on a course page.');
    }
});
