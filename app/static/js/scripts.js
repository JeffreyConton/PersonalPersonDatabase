$(document).ready(function() {
    let page = 2;
    let loading = false;

    function loadMorePeople() {
        if (loading) return;
        loading = true;
        $('#loading').show();
        $.get('/browse', { page: page, ajax: 1 }, function(data) {
            $('#loading').hide();
            console.log('Received data:', data);  // Debug statement to check the received data
            if (data.people.length > 0) {
                data.people.forEach(function(person) {
                    $('#people-container').append(
                        '<div class="col-md-4 mb-4">' +
                        '<div class="card bg-secondary text-white h-100">' +
                        '<div class="card-body d-flex flex-column">' +
                        '<h5 class="card-title">' + person.full_name + '</h5>' +
                        '<p class="card-text">' + person.email_address + '<br>' + person.phone_number + '</p>' +
                        '<div class="mt-auto">' +
                        '<a href="/edit/' + person.id + '" class="btn btn-secondary"><i class="fas fa-edit"></i> Edit</a>' +
                        '<form action="/delete/' + person.id + '" method="post" style="display:inline;">' +
                        '<button type="submit" class="btn btn-danger"><i class="fas fa-trash"></i> Delete</button>' +
                        '</form>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '</div>'
                    );
                });
                page++;
                loading = false;
            } else {
                $(window).off('scroll', onScroll);
            }
        }).fail(function() {
            $('#loading').hide();
            loading = false;
        });
    }

    function onScroll() {
        if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
            loadMorePeople();
        }
    }

    $(window).on('scroll', onScroll);
});