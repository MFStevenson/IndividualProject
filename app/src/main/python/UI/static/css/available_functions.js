// variables will be changed to get these lists from backend dictionary
// will use the list at the specified key
// note: might need to change some names around, need to work out how to
// link radio button to function
var descTests = ["mean and standard deviation"]
var vis = ["regression_plt"]
var infTests = ["regression"]

function showDescOptions() {
    for (var test in descTests){
        $('#descTestsButton').append(
            $('<input>').prop({
                type: 'radio',
                id: test,
                name: 'descOptions',
                value: test
            })
        ).append(
            $('<label>').prop({
                for: value
            }
            )
        ).append(
        $('<br>')
        );
    }
};

function showVisOptions() {

}

function showInfOptions() {
    
}