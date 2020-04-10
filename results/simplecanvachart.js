function SimpleCanvaChart(title,div,data,colors,height,width,type) {
	if (data.length == colors.length) {
		div.innerHTML = '<canvas></canvas>';
		canvas = div.children[0];
		canvas.width = width;
		canvas.height = height;
		canvas.style.border = '1px solid';

		min = data[0][0];
		max = data[0][0];

		for (var i = data.length - 1; i >= 0; i--) {
			for (var j = data[i].length - 1; j >= 0; j--) {
				if (data[i][j] > max) {
					max = data[i][j];
				}
				if (data[i][j] < min) {
					min = data[i][j];
				}
			}
		}

		interval = max-min;
		min = min-(interval*0.1);
		max = max+(interval*0.1);
		interval = max-min;

		console.log('Min: '+parseFloat(min)+'; Max: '+parseFloat(max)+'; Interval: '+parseFloat(interval));

		ctx = canvas.getContext('2d');

		dx = width/data[0].length;

		if (type[1]) {

			for (var i = data.length - 1; i >= 0; i--) {
				for (var j = data[i].length - 1; j >= 0; j--) {
					y = (data[i][j]-min)*(height/interval);
					x = j*dx+(dx/2);
					ctx.strokeStyle = 'lightgray';
					ctx.moveTo(x,height-y);
					if (typeof data[i][j+1] != 'undefined') {
						y2 = (data[i][j+1]-min)*(height/interval);
						x2 = (j+1)*dx+(dx/2);
						ctx.lineTo(x2,height-y2);
						ctx.stroke();
					}
				}
			}

		}

		if (min <= 0 || max >= 0) {
			y = (0-min)*(height/interval);
			x = 0;

			ctx.moveTo(x,height-y);
			ctx.lineTo(width,height-y);
			ctx.strokeStyle = 'black';
			ctx.stroke();
			ctx.fillStyle = 'black';
			ctx.font = "10px Arial";
			ctx.fillText('Zero (0)',x+5,height-y-5);
		}

		if (type[0]) {

			for (var i = data.length - 1; i >= 0; i--) {
				for (var j = data[i].length - 1; j >= 0; j--) {
					y = (data[i][j]-min)*(height/interval);
					x = j*dx+(dx/2);
					ctx.fillStyle = colors[i];
					ctx.fillRect(x-5,height-y-5,10,10);
				}
			}

		}

		ctx.fillStyle = 'black';
		ctx.font = "20px Arial";
		ctx.fillText(title, 20, 40);
	}
}