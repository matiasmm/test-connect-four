function Game(baseUrl, user_id, $table, $){
    var turn,
        data = [],
        $container = $($table.find('tbody'));

    function main (){
        update_status();
        refresh_turn(user_id == 1? true : false);
    }

    function click(row){
        alert(row);
    }

    function refresh_turn(v){
        turn = v;
        if (turn) {
            $table.find('thead button').removeAttr('disabled');
        }else{
            $($table.find('thead button')).attr('disabled','disabled');
        }
    }

    function draw(){
        var r, c, $tr, $td, $el;
        $container.html('');
        for(r = data.length; r >= 0; r--) {
            $tr = $('<tr>').attr('row', r);
            for(c = data.length; c >= 0; c--) {
                $el = $('<div class="circle">').attr('col', c).attr('row', r);
                $td = $('<td>').append($el);
                $tr.prepend($td);
            }
            $container.prepend($tr);
        }
    }

    function update_status(){
        $.ajax({'url': baseUrl + 'api/status',
            success: function(resp) {
                var col, row, k;
                for(k in resp) {
                    row = resp[k].row;
                    col = resp[k].col;
                    if(data[row] == undefined) {
                        data[row] = [];
                    }
                    data[row][col] =  resp[k].player_id;
                }

                draw();
            }
        })
    }

    main();

    this.click = click;
    this.click = draw;
    this.data = data;
}