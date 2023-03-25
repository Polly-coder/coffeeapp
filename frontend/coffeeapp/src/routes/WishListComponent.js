import React, { Component } from 'react'

export default class WishListComponent extends Component {
    constructor(props) {
      super(props)
    
      this.state = {
         listPlaces: [
            { name: 'Mad',
             isComplited: false
            },
            { name: 'Fika',
             isComplited: false
            },
            { name: 'Doris',
             isComplited: false
            }
         ]
     }

      this.addPlace = this.addPlace.bind(this);
      this.updateList = this.updateList.bind(this);
    }

    updateList(index, value){
        this.setState({
            listPlaces: this.state.listPlaces.map((place, ind)=>{
                if (ind == index){ //index - string, тк из Id
                    return Object.assign({}, place, {isComplited: value})
                }
                return place;
            })
        })
    }

    addPlace(place){
        this.setState({
            name: place.name,
            isComplited: false
        })
    }


  render() {
    return (
      <div className='container '>
        <div className='mt-3 text-center'>
              <h2>Вишлист:</h2>
        </div>
        <div className='mx-auto w-50'>
          
            {this.state.listPlaces.map((place, index)=>
            <div class="form-check" key={index}>
            <input
              id={index}
              type="checkbox"
              className="form-check-input"
              checked={place.isCompleted}
              onChange={(event) => this.updateList(event.target.id, event.target.checked)} />
              <label className="form-check-label" for={index}>
                {place.name}
              </label>
              
            </div>)}
        </div>
        
          
      </div>
    )
  }
}
