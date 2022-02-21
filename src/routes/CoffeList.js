import React, { Component } from 'react';
import {list_places} from '../places';

export default class CoffeList extends Component {
    constructor(props) {
        super(props)
      
        this.state = {
           places: list_places
        }

        this.new_tags = (arr=list_places)=>{
          let new_arr = [];
          for (let list_tags of arr.map((place)=>place.tag)){
            
            if (list_tags && Array.isArray(list_tags)){
              for (let one_tag of list_tags){
                if (new_arr.indexOf(one_tag)== - 1){
                  console.log(one_tag);
                  new_arr.push(one_tag);
                }
              }

            }
            
          }
          return new_arr;
        }
        
        this.handleChange = this.handleChange.bind(this);
      }
    
      handleChange(event){
          let tag = event.target.value;
          const tags = list_places.map((place)=>place.tag);
          let newPlaces = [];
          if (tag=='all'){
            this.setState({
              places: list_places
            })
          }
          else{
            for (let i = 0; i<tags.length; i++){
              if (tags[i] && tags[i].indexOf(tag) != -1){
                newPlaces.push(list_places[i]);
              }
            }
            this.setState({
              places: newPlaces
            })
          }
    
          
          
      }
    
      render(){
        return (
        <div className='container'>
            <div className='mt-3 text-center'>
              <h2>Кофейни:</h2>
            </div>
            
            <div className='mb-3'>
              <label for="tags" class="form-label mt-4">Категория</label>
              <select className=' form-select' id='tags' onChange={this.handleChange}>
                {this.new_tags().map((tag, index)=>
                    <option key={index} value={tag}>{tag}</option>)
                  
                }
                <option value="all" selected>Все</option>
              </select>
            </div>

            <ul className='list-group list-group-flush'>
              {this.state.places.map((place, index)=><li className='list-group-item' key={index} >
                <div className='row mx-auto'>
                  
                  <div className='col col-sm-4'>
                    <h4>
                      {place.name}
                    </h4>
                    <p>{place.description}</p>
                    <p>{place.adress}</p>
                    <button type="button" class="btn btn-outline-secondary">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                      </svg>
                    </button>
                  </div>
                  <div className='col col-sm-8'>
                    <img src={place.image} className="d-flex rounded mx-auto" style={ {width: '50%'} }></img>
                  </div>
                </div>                
                </li>
              )}
            </ul>
        </div>
      );
      }
}
