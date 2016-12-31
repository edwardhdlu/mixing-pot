$(document).ready(function() {
	total = 0;

	// fetch ingredients
	var ingredients = [];
	ingredients_src = "https://raw.githubusercontent.com/edwardhdlu/Cooking-Papa/master/data/ingredients.txt";
	
	var req1 = $.get(ingredients_src, function(data) { 
		ingredients = data.split("\n");
	});

	// fetch scores
	var scores = {};
	scores_src = "https://raw.githubusercontent.com/edwardhdlu/Cooking-Papa/master/data/scores.txt";
	var req2 = $.get(scores_src, function(data) {
		var lines = data.split("\n");
		for (var i = 0; i < lines.length; i++) {
			var arr = lines[i].split(",");

			if (!(arr[0] in scores)) {
				scores[arr[0]] = {};
			}
			if (!(arr[1] in scores)) {
				scores[arr[1]] = {};
			}
			scores[arr[0]][arr[1]] = arr[2];
			scores[arr[1]][arr[0]] = arr[2];
		}
	});

	// wait for fetches to complete
	$.when(req1, req2).done(function() {
		var active = [];
		var results = [];
		$("#not-loaded").hide();

		// pick 3 random ingredients to start
		var len = ingredients.length;
		while (active.length < 3) {
			r = Math.floor(Math.random() * len - 1);
			if (!active.includes(ingredients[r])) {
				active.push(ingredients[r]);
			}
		}

		for (var i = 0; i < active.length; i++) {
			$("#active-ingredients").append("<li>" + active[i] + "</li>");
		}

		// autocomplete
		$("#suggester").keyup(function() {
			var query = $(this).val();
			results = ingredients.filter(function(i) {
				return i.includes(query) && query != "";
			});

			$("#search-results").empty();
			for (var i = 0; i < results.length; i++) {
				var button = "<a class='add-button"
				if (active.includes(results[i])) {
					button += " inactive";
				}
				button += "'></a>";

				$("#search-results").append("<li>" + results[i] + button + "</li>");
			}
		});

		// add ingredient
		$(document).on("click", ".add-button:not(.inactive)", function(e) {
			$(this).addClass("inactive");

			var ingredient = $(this).parent().text();
			active.push(ingredient);

			$("#active-ingredients").empty();
			for (var i = 0; i < active.length; i++) {
				var score = "";
				if (ingredient != active[i]) {
					var val = scores[ingredient][active[i]] != null ? scores[ingredient][active[i]] : -20;
					score = "<span class='li-score'>" + (val > 0 ? "+" : "") + val + "</span>";
					total += parseInt(val);
				}

				$("#active-ingredients").append("<li>" + active[i] + score + "</li>");
			}

			$("#score").text(total);

			if (total < -200) {
				$("#end-score").text(active.length);
				$("#game-over").show();
			}
		});

	});

});