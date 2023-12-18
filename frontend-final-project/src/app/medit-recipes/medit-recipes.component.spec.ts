import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MeditRecipesComponent } from './medit-recipes.component';

describe('MeditRecipesComponent', () => {
  let component: MeditRecipesComponent;
  let fixture: ComponentFixture<MeditRecipesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MeditRecipesComponent]
    });
    fixture = TestBed.createComponent(MeditRecipesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
