import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AsianRecipesComponent } from './asian-recipes.component';

describe('AsianRecipesComponent', () => {
  let component: AsianRecipesComponent;
  let fixture: ComponentFixture<AsianRecipesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AsianRecipesComponent]
    });
    fixture = TestBed.createComponent(AsianRecipesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
