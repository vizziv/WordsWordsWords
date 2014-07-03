var letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

var width = 600;
var height = 400;

var svg = d3.select('.chart')
    .append('svg')
    .attr('width', width)
    .attr('height', height);

var data = [1,1,2,3,5,8,13,21,35];

var y = d3.scale.linear()
    .domain([0, d3.max(data)])
    .range([0, height])

var x = d3.scale.ordinal()
    .domain(letters)
    .rangeRoundBands([0, width], .1)

function pushData(xs) {
    var bars = svg.selectAll('rect').data(xs)
    bars.exit().remove()
    bars.enter().append('rect')
        .attr('x', function(d, i) { return x(letters[i]); })
        .attr('width', x.rangeBand())
        .attr('height', y)
        .attr('y', 0)
    bars
        .attr('height', y)
}

pushData(data)
