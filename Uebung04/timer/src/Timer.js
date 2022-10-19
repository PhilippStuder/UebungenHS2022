import React,{Component} from "react";

class Timer extends Component{
    constructor(props){
        super(props);

        this.interval = null;
        this.state = {count: this.props.startvalue};
        // this.state = this.props.startvalue;

        this.update = this.update.bind(this);
        this.timer = this.timer.bind(this);

    }

    update(){
        this.setState({count : this.state.count - 1});
        // this.setState(this.state=this.state-1);
        if (this.state.count <= 1){
            this.setState({count:"FERTIG!!!"});
            clearInterval(this.interval)
            this.interval = null;
        }
    }


    timer(){
        this.setState({count: this.props.startvalue});

        if (this.interval != null){
            clearInterval(this.interval);
        }

        this.interval = setInterval(this.update,1000);
    }

  

    render(){
        return(<>
            <p>Starten sie den Timer mit dem Button.</p>
            <p><button onClick={this.timer}>Start</button></p>
            <p>{this.state.count}</p>

        </>)
    }

}
export default Timer;