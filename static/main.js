function Game(baseUrl, user_id, $table, $){
    var turn;

    function main (){
        refresh_turn(user_id == 1? true : false);
    }

    function click(row){
        alert(row);
    }

    function refresh_turn(v){
        turn = v;
        if (turn) {
            $table.find('thead button').removeAttr('disabled');;
        }else{
            $($table.find('thead button')).attr('disabled','disabled');
        }

    }

    main();

    this.click = click;
}