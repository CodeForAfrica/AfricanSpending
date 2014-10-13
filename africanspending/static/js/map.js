$(function() {
    var $map = $('#map'),
        mapLinks = $map.data('map-links'),
        mapSelect = $map.data('map-select');

    var drawMap = function($dfd) {
        var width = $map.width(),
            height = width * 1;
        
        $map.height(height); 
        
        var svg = d3.select("#map").append("svg")
            .attr("width", width)
            .attr("height", height);

        var projection = d3.geo.orthographic()
            .scale(width * 0.7)
            .translate([width / 3, height / 2])
            .clipAngle(90)
            .precision(.1);
        var path = d3.geo.path()
            .projection(projection);
        
        $dfd.then(function(mapData) {
            var countries = topojson.feature(mapData, mapData.objects.subunits);
            svg.selectAll(".country")
                    .data(countries.features)
                .enter().append("path")
                    .attr("class", function(d) {
                        var clazz = "country " + d.id;
                        if (d.id == mapSelect) {
                            clazz = "selected " + clazz;
                        }
                        return clazz;
                    })
                    .attr("d", path)
                    .on("click", function(d) {
                        var path = mapLinks[d.id];
                        if (path) {
                            window.location = path;
                        }
                    })
                    .on("mouseenter", function(d) {
                        var self = d3.select(this);
                        d.baseClass = self.attr('class');
                        self.attr('class', d.baseClass + ' hovered');
                    })
                    .on("mouseleave", function(d) {
                        var self = d3.select(this);
                        self.attr('class', d.baseClass);  
                    });

            if (!mapSelect) {
                svg.append("path")
                    .datum(topojson.feature(mapData, mapData.objects.places))
                    .attr("d", path)
                    .attr("class", "place");

                svg.selectAll(".place-label")
                        .data(topojson.feature(mapData, mapData.objects.places).features)
                    .enter().append("text")
                        .attr("class", "place-label")
                        .attr("transform", function(d) { return "translate(" + projection(d.geometry.coordinates) + ")"; })
                        .attr("dy", ".35em")
                        .attr("x", function(d) { return d.geometry.coordinates[0] > -1 ? 6 : -6; })
                        .style("text-anchor", function(d) { return d.geometry.coordinates[0] > -1 ? "start" : "end"; })
                        .text(function(d) { return d.properties.name; });    
            }
            
        });
    };

    if($map.length) {
        var $dfd = $.getJSON('/static/maps/africa.json'),
            resizeTimeout;
        drawMap($dfd);
        $(window).resize(function() {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(function() {
                $map.empty();
                drawMap($dfd);
            }, 100);
        });
    }
});
