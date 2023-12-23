import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FavRecipeComponent } from './fav-recipe.component';

describe('FavRecipeComponent', () => {
  let component: FavRecipeComponent;
  let fixture: ComponentFixture<FavRecipeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FavRecipeComponent]
    });
    fixture = TestBed.createComponent(FavRecipeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
