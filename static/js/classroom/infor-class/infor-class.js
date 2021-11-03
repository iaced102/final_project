function register_class()
            {
                if('{{ request.user.is_authenticated }}'=='False')
                    {
                        alert("Bạn cần đăng nhập để đăng kí vào lớp học");
                        window.location.replace("{% url 'login' %}");
                    }
                else
                    {
                        $.ajax({
                            url: "{% url 'join_to_class' %}",
                            method: "POST",
                            data: {
                                'csrfmiddlewaretoken': '{{ csrf_token }}',
                                'class': '{{classroom.id}}'
                                },
                            success: function(result){
                                if(result === 'success')
                                    {
                                        alert('đăng kí thành công')
                                        //window.location.replace("{% url 'home' %}");
                                    }
                                else
                                    {
                                        alert('bạn đã ở trong lớp này rồi')
                                        //window.location.replace("{% url 'home' %}");
                                    }
                            }
                        })           
                    }
        }