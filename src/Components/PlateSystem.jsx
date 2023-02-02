import react from 'react';

const PlateSystem = () => {

	var weights = {
		25 : 0,
		20 : 2,
		15 : 1,
		10 : 1,
		5  : 1,
	}

	// TODO: something went wrong here…
	function calculate(target, bar=20) {
		target -= bar;
		var plates = [];

		for (const [w, wVal] of Object.entries(weights)) {
			// Ignores plate if it exceeds weight target
			if ((target - (w * 2)) < 0) {
				continue;
			}

			// Adds appropriate plate
			let combined = w * 2;
			let num = Math.floor(target/combined);
			if (wVal >= num) {
				plates += [w] * num;
				target -= combined * num;
			} else {
				plates += [w] * wVal;
				target -= combined * wVal;
			}

		console.log(plates);
		console.log("hello")
		return "hello";
		}
	}

	const Plate = ({props}) => {
		return(
			<span>This is a weight</span>	
		);
	}

	return(
		<div className="plate-system">
			<h1>Plate System</h1>
			<Plate/>
			<Plate/>
			<Plate/>
			<script>{calculate(100)}</script>
		</div>	
	);

}

export default PlateSystem;