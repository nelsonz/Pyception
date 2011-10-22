$(window).load(function() {
	
	draw = function(types, div) {
	    for (var name in types) {
		var alttext = types[name]['doc'];
		var randX = Math.floor(Math.random()*450); 
		var randY = Math.floor(Math.random()*300);
		types[name]['el'] =  $("<div></div>").data('info', {name: name, x: randX, y: randY, fruit: types[name]}).addClass(div).css({left: randX, top: randY}).toggle(function(){
			var data = $(this).data('info');
			expand(data.fruit, data.x, data.y);
		    }, function(){
			var data = $(this).data('info');
			removeChildren(data.fruit);
		    }).appendTo("#growsOnTrees");
	    }
	}
	
	expand = function(current, x, y) {
	    var count = 0;
	    for (var key in current) {
		count += 1;
	    }
	    var increment = 2 * Math.PI / count;
	    var length = 80;
	    var angle = 0;
	    if (current.hasOwnProperty('classes')) {
		for (var name in current['classes']) {
		    console.log(angle * 180 / (2 * Math.PI));
		    var newX = x + length * Math.cos(angle);
		    var newY = y - length * Math.sin(angle);
		    current['classes'][name]['el'] =  $("<div></div>").data('info', {name: name, x: newX, y: newY, fruit: current["classes"][name]}).addClass("classFruit").css({left: newX, top: newY}).click(function(){
			    var data = $(this).data('info');
			    expand(data.fruit, data.x, data.y);
			}, function(){
			    var data = $(this).data('info');
			    removeChildren(data.fruit);
			}).appendTo("#growsOnTrees");
		    
		    angle += increment;
		}
	    }
	    
	    if (current.hasOwnProperty('functions')) {
		for (var name in current['functions']) {
		    console.log(angle * 180 / (2 * Math.PI));
		    var newX = x + length * Math.cos(angle);
		    var newY = y - length * Math.sin(angle);
		    current['functions'][name]['el'] =  $("<div></div>").data('info', {name: name, x: newX, y: newY, fruit: current["functions"][name]}).addClass("classFruit").css({left: newX, top: newY}).click(function(){
			    var data = $(this).data('info');
			    expand(data.fruit, data.x, data.y);
			}, function(){
			    var data = $(this).data('info');
			    removeChildren(data.fruit);
			}).appendTo("#growsOnTrees");
		    
		    angle += increment;
		}
	    }
	    
	    if (current.hasOwnProperty('variables')) {
		for (var name in current['variables']) {
		    console.log(angle * 180 / (2 * Math.PI));
		    var newX = x + length * Math.cos(angle);
		    var newY = y - length * Math.sin(angle);
		    current['variables'][name]['el'] =  $("<div></div>").data('info', {name: name, x: newX, y: newY, fruit: current["variables"][name]}).addClass("classFruit").css({left: newX, top: newY}).click(function(){
			    var data = $(this).data('info');
			    expand(data.fruit, data.x, data.y);
			}, function(){
			    var data = $(this).data('info');
			    removeChildren(data.fruit);
			}).appendTo("#growsOnTrees");
		    
		    angle += increment;
		}
	    }
	}
	
	removeChildren = function(current) {
	    for(var key in current.classes) {
		removeChildren(current.classes[key]);
		if(current.classes[key].el) {
		    current.classes[key].el.remove();
		}
	    }
	    for(var key in current.functions) {
		removeChildren(current.functions[key]);
		if(current.functions[key].el) {
		    current.functions[key].el.remove();
		}
	    }
	    for(var key in current.variables) {
		removeChildren(current.variables[key]);
		if(current.variables[key].el) {
		    current.variables[key].el.remove();
		}
	    }
	}
	
	$('.classFruit, .varFruit, .methodFruit').click(function() {
		
		$('#pushThisButton').click(function() {
			$('#semiRelevantInfo').slideToggle('slow', function() {
				$('#editor, #containsCodeEditor').css({ 'height' : '500px' });
				editor = ace.edit("editor");
				var PythonMode = require("ace/mode/python").Mode;
				editor.getSession().setMode(new PythonMode());
				$('#showForm').animate({ 'opacity' : '1' });
			    });
		    });
		
		$('#smallify').click(function() {
			$.post('/transferCode/', {'code': editor.getSession().getValue()}, 
			       
			       function(dic) {
				   all = dic;
				   console.log( all );
				   
				   draw(all.classes, 'classFruit');
				   draw(all.variables, 'varFruit');
				   draw(all.functions, 'methodFruit');
			       });
			
			$('#showFrom').animate({ 'opacity' : '0' });
			$('#editor, #containsCodeEditor').css({ 'height' : '0px' });
			
			$('#contentButNotHappy').fadeToggle('slow');
			$('#contentAndNotSad').fadeToggle('slow');
			
		    });
	    });
    