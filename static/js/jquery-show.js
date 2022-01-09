<script>

    $(document).ready(function() {
        $("#A propos").click(function(){
            if ($('#about').is(":hidden")){
                $("#about").slideDown('slow');
            }else{
                $('#about').slideUp('slow');
            }
        });
    });

</script>