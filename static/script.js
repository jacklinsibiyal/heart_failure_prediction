document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        if (validateForm()) {
            this.submit();
        }
    });

    function validateForm() {
        let isValid = true;
        const numericFields = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak'];
        
        numericFields.forEach(field => {
            const input = document.getElementById(field);
            const value = input.value.trim();
            
            if (value === '' || isNaN(value)) {
                showError(input, `Please enter a valid number for ${field}`);
                isValid = false;
            } else {
                clearError(input);
            }
        });

        return isValid;
    }

    function showError(input, message) {
        input.classList.add('error');
        let errorDiv = input.nextElementSibling;
        if (!errorDiv || !errorDiv.classList.contains('error-message')) {
            errorDiv = document.createElement('div');
            errorDiv.classList.add('error-message');
            input.parentNode.insertBefore(errorDiv, input.nextSibling);
        }
        errorDiv.textContent = message;
    }

    function clearError(input) {
        input.classList.remove('error');
        const errorDiv = input.nextElementSibling;
        if (errorDiv && errorDiv.classList.contains('error-message')) {
            errorDiv.remove();
        }
    }
});