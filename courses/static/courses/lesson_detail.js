document.addEventListener('DOMContentLoaded', function () {
    const courseInfo = document.getElementById('course-info');
    if (courseInfo) {
        var totalLessons = parseInt(courseInfo.dataset.totalLessons, 10);
        var completedLessons = parseInt(courseInfo.dataset.completedLessons, 10);

        if (isNaN(totalLessons) || isNaN(completedLessons)) {
            return;
        }
    } 

    // Handler for the "Complete Lesson" button
    const completeLessonButton = document.querySelector('#complete-lesson-button');
    if (completeLessonButton) {
        completeLessonButton.addEventListener('click', function () {
            const lessonId = this.dataset.lessonId;
            if (lessonId) {
                markLessonAsCompleted(lessonId);
            } 
        });
    } 

    // Progress update
    updateProgressBar();

    function markLessonAsCompleted(lessonId) {
        fetch(`/complete_lesson/${lessonId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
        .then(response => {
            if (response.ok) {
                alert('Lesson completed successfully!');

                //Updating a button to make it inactive
            const completeLessonButton = document.querySelector('#complete-lesson-button');
            if (completeLessonButton) {
                completeLessonButton.textContent = 'Completed';
                completeLessonButton.disabled = true;
            }
                completedLessons += 1; 
                updateProgressBar(); 
            } else {
                alert('Error completing lesson. Please try again.');
            }
        })
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function updateProgressBar() {
        const progressBar = document.querySelector('.progress-bar');
        if (progressBar) {
            if (totalLessons > 0) {
                const progressPercentage = Math.min((completedLessons / totalLessons) * 100, 100);

                progressBar.style.width = `${progressPercentage}%`;
                progressBar.setAttribute('aria-valuenow', progressPercentage);    
            }
        }
    }
});
